
class Solution:

    def unique_emails(self, emails: []) -> int:

        clean_email_set = set()

        for email in emails:

            local, domain = email.split('@')

            clean_local = "".join(local.split('+')[0].split('.'))
            clean_email = clean_local + '@' + domain
            clean_email_set.add(clean_email)

        return len(clean_email_set)




