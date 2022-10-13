import httpx

url = r'https://gist.githubusercontent.com/arrayJY/6ceb79ea0f9b9f5675b288b6a135038e/raw/73d839c01482e360ad4f72ea1d5a34db52fd046f/%25F0%259F%2593%258A%2520Weekly%2520development%2520breakdown'

r = httpx.get(url)

print(r.text)


base_str = ""
with open('README_base.md', 'r') as f:
    base_str = f.read()

with open('README.md', 'w') as f:
    f.write(base_str)

with open('README.md', 'a') as f:
    f.writelines([
        "```\n",
        "Weekly Development Breakdown\n",
        "\n",
        r.text,
        "\n"
        "```\n"
    ])


