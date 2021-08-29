favorite_languages = {
    'jen': 'python',
    'jamie': 'c',
    'josh w.': 'ruby',
    'josh h.': 'python'
    }

poll_people = ['mom', 'jamie', 'dad', 'jen', 'Brandon', 'Landyn']
for poller in poll_people:
    if poller not in favorite_languages:
        print(poller.title() + ", come take my 'favorite language' poll!")
    else:
        print(poller + ", thank for taking the poll!")
