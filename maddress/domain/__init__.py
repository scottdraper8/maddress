# DEPENDENCIES
# -------------------------------------------------------------------------------------------------------------------------------- #
from .domain_dict import domains
# -------------------------------------------------------------------------------------------------------------------------------- #


# DEFINE BINARY SEARCH ALGORITHIM
# -------------------------------------------------------------------------------------------------------------------------------- #
def binary_search(arr, e):
    # -- List index vars -- #
    low = 0
    high = len(arr) - 1
    mid = 0

    # -- Half the list each search -- #
    while low <= high:
        mid = (high + low) // 2

        # -- Search for the value at a given key -- #
        if arr[mid] < e:
            low = mid + 1

        elif arr[mid] > e:
            high = mid - 1

        else:
            return mid

    # -- If the element reaches here, then the element was not present -- #
    return False
# -------------------------------------------------------------------------------------------------------------------------------- #


# CHECK IF DOMAIN OR EMAIL
# --------------------------------------------------------------------------------------------------------------------------------
def domain_or_email(arg):
    arg = arg.strip()
    if arg.__contains__('@') and arg.__contains__('.') and arg[0] != '.' and arg[0] != '@' and not arg.isspace():
        return 'email'
    elif not arg.__contains__('@') and arg.__contains__('.') and arg[0] != '.' and arg[0] != '@' and not arg.isspace():
        return 'domain'
    else:
        raise Exception('Not a vaild domain or email')
# -------------------------------------------------------------------------------------------------------------------------------- #


# EXTRACT DOMAIN FROM EMAIL
# -------------------------------------------------------------------------------------------------------------------------------- #
def domain_extractor(email):
    if domain_or_email(email) == 'email':
        return email.split('@')[1].lower().strip()
    else:
        raise Exception('Not a valid email')
# -------------------------------------------------------------------------------------------------------------------------------- #


# CHECK THE DOMAIN TYPE
# -------------------------------------------------------------------------------------------------------------------------------- #
def domain_type(domain):
    # -- Ensure the domain arg is a domain. If not, convert email to a domain -- #
    if domain_or_email(domain) == 'email':
        domain = domain_extractor(domain)
    else:
        domain = domain

    # -- Return the domain type -- #
    if binary_search(domains['generic'], domain):
        return 'generic'
    elif binary_search(domains['personal'], domain):
        return 'personal'
    else:
        return 'Unknown'
# -------------------------------------------------------------------------------------------------------------------------------- #


# EXCLUDE DOMAINS BASED ON GIVEN CRITERIA
# -------------------------------------------------------------------------------------------------------------------------------- #
def domain_excluder(arr, exclude=[]):
    # -- Ensure the "exclude" arg is correctly formatted -- #
    if type(exclude) == list:
        if len(exclude) > 3 or len([x for x in exclude if x.lower().strip() != 'personal' and x.lower(
        ).strip() != 'generic' and x.lower().strip() != 'gov']) > 0:
            raise Exception(
                '"exclude" tag must be a list with any or all of the following values: "personal", "generic", or "gov"')
    else:
        raise Exception(
            '"exclude" tag must be a list with any or all of the following values: "personal", "generic", or "gov"')
    exclude = [x.lower().strip() for x in exclude]

    # -- Determine the exlcusion logic to be run -- #
    exclude_gov = False
    if 'gov' in exclude:
        exclude.remove('gov')
        exclude_gov = True

    # -- Create list of preserved domains -- #
    preserved = []
    for i, domain in enumerate(arr):
        # -- Ensure the domain arg is a domain. If not, convert email to a domain -- #
        if domain_or_email(domain) == 'email':
            domain = domain_extractor(domain)
        else:
            domain = domain.lower().strip()

        if not exclude_gov:
            for x in exclude:
                if not binary_search(domains[x], domain):
                    preserved.append(arr[i])
                else:
                    pass
        elif exclude_gov and not domain.__contains__('gov'):
            preserved.append(arr[i])

    return preserved
# -------------------------------------------------------------------------------------------------------------------------------- #
