import gitlab

# anonymous read-only access for public resources (GitLab.com)
gl = gitlab.Gitlab()

# anonymous read-only access for public resources (self-hosted GitLab instance)
gl = gitlab.Gitlab('https://repo.vietis.com.vn:8009')

# private token or personal token authentication (GitLab.com)
gl = gitlab.Gitlab(private_token='glpat-yoEBMM5V5GyW2vMY4zRQ')

# private token or personal token authentication (self-hosted GitLab instance)
gl = gitlab.Gitlab(url='https://repo.vietis.com.vn:8009', private_token='glpat-yoEBMM5V5GyW2vMY4zRQ')

# oauth token authentication
users = gl.users.list()