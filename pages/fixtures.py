class fixtures_c:
    class users:
        valid_creds = {'username': 'vrem_test', 'password': 'time_test123'}
        invalid_creds = {'username': 'vrem_test', 'password': 'time_test456'}

    class mail:
        recipient = 'vrem_test@mail.ru'
        body = '''DEAR MADAM:

Last evening, owing to a drunken debauch, for which I have no
satisfactory or suitable explanation to make, I was the unfortunate
occasion of an outrage upon your feelings and those of your daughter
and friends, for which I wish most humbly to apologize.  I cannot
tell you how sincerely I regret whatever I said or did, which I
cannot now clearly recall.  My mental attitude when drinking is
both contentious and malicious, and while in this mood and state
I was the author of statements which I know to be wholly unfounded.
In my drunken stupor I mistook you for a certain notorious woman
of Louisville--why, I have not the slightest idea.  For this wholly
shameful and outrageous conduct I sincerely ask your pardon--beg
your forgiveness.  I do not know what amends I can make, but
anything you may wish to suggest I shall gladly do.  In the mean
while I hope you will accept this letter in the spirit in which
it is written and as a slight attempt at recompense which I know
can never fully be made.

Very sincerely,

BEALES CHADSEY.
'''
