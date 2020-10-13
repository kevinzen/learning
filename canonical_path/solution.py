
# not from end:
# 1 => 1
# 2 => 1
# 3 => 2
# 4 => 2
# 5 => 3
# 6 => 3
# 7 => 4
# n => n // 2 + n % 2
# if end seat then n, else n // 2 + n % 2



from collections import deque
import re


class Solution:

    def simplify_path(self, path: str) -> str:

        # example = '/a//b//./c/d/../d/e//.////.//'
        # 1. remove duplicate slashes (can be more than once) - '/a/b/./c/d/../d/e/././'
        # 2. strip trailing slash
        # 3. remove '/.' tokens as they are meaningless (search for '/./' and '/.$' elements
        # 4. Get to reduced form: '/a/b/c/d/../d/e' - '/a//b//./c/d/../d/e//.////.'

        # example: '/a//b//./c/d/../d/e//.////.//'
        len_after = len_before = None
        while(len_after is None or len_before != len_after):
            len_before = len(path)
            path = path.replace('//', '/')
            len_after = len(path)

        print("3 - path = " + path)

        len_after = len_before = None
        while(len_after is None or len_before != len_after):
            len_before = len(path)
            path = path.replace('/./', '/')
            len_after = len(path)
        # path should now be: '/a/b/./c/d/../d/e/././' --> Now get rid of '/.' elements
        path = re.sub('/\.$', '', path)   # in case it's at the end

        # path should now be: '/a/b/c/d/../d/e/' -> strip trailing '/' if there
        path = re.sub('/$', '', path)   # in case it's at the end

        # path should now be: '/a/b/c/d/../d/e' -> break into pieces and put them on a stack

        path_elements = deque(path.split('/'))

        # path_elements should now be deque(['a', 'b', 'c', 'd', '..', 'd', 'e'])
        # now process them to simplify and get rid of '..' elements
        final_path_elements = deque('/')
        while path_elements:
            element = path_elements.popleft()

            if element == '..':
                if len(final_path_elements) > 1:
                    final_path_elements.pop()
            elif len(element) == 0:
                pass
            else:
                final_path_elements.append(element)

        final_path = "/".join(final_path_elements)
        final_path = final_path.replace("//","/")

        return final_path



