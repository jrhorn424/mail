#!/usr/bin/python
import re, subprocess
def get_keychain_pass(account=None, server=None):
    params = {
            'security': '/usr/bin/security',
            'command': 'find-internet-password',
            'account': account,
            'server': server,
            'keychain': '/Users/jeffh/Library/Keychains/login.keychain',
            }
    command = "sudo -u jeffh %(security)s -v %(command)s -g -a %(account)s -s %(server)s %(keychain)s" % params
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    outtext = [l for l in output.splitlines()
            if l.startswith('password: ')][0]

    return re.match(r'password: "(.*)"', outtext).group(1)

# nametrans helpers
l2r_mapping = {
  'inbox': 'INBOX'
, 'drafts': 'INBOX.Drafts'
, 'junk': 'INBOX.Junk Mail'
, 'sent': 'INBOX.Sent Items'
, 'trash': 'INBOX.Trash'
, 'sane/blackhole': 'INBOX.+SaneBlackHole'
, 'sane/bulk': 'INBOX.+SaneBulk'
, 'sane/community': 'INBOX.+SaneCommunity'
, 'sane/date': 'INBOX.+SaneDate'
, 'sane/deals': 'INBOX.+SaneDeals'
, 'sane/github': 'INBOX.+SaneGitHub'
, 'sane/later': 'INBOX.+SaneLater'
, 'sane/learning': 'INBOX.+SaneLearning'
, 'sane/news': 'INBOX.+SaneNews'
, 'sane/social': 'INBOX.+SaneSocial'
, 'archive/coupons': 'INBOX.Archive.Coupons'
, 'archive/hold': 'INBOX.Archive.Hold'
, 'archive/vacation': 'INBOX.Archive.Vacation'
, 'archive': 'INBOX.Archive'
}

r2l_mapping = { val: key for key, val in l2r_mapping.items() }

def nt_remote(folder):
    try:
        return r2l_mapping[folder]
    except:
        return folder

def nt_local(folder):
    try:
        return l2r_mapping[folder]
    except:
        return folder


def is_included(folder):
  result = True

  for pattern in exclusion_patterns:
    result = result and (re.search(pattern, folder) == None)

  return result

exclusion_patterns = [
  'RESTORED'
]
