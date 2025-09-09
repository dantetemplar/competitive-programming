
## Scaffolding from page of contest

I suggest to use my version of [Competitive Programming Helper](https://github.com/dantetemplar/fork-cph) (get VSIX file from [Releases](https://github.com/dantetemplar/fork-cph/releases)) vscode extension and [Competitive Companion](https://github.com/jmerle/competitive-companion#readme) browser extension to scaffold the code for the contest – you will need to click extension logo in browser to get whole problem set with testcases right in your IDE.

It will create a several files with templates for the contest. You can see my template in [_cph_template.py](_cph_template.py).

<i>Actually, I made a pull request https://github.com/agrawal-d/cph/pull/582 to the original repository, it is in review now.</i>

#### Faster I/O

Template contains faster I/O code to speed up bottlenecks on Codeforces platform:

```python
import sys

def input():
    """
    Faster input in 25 times on 1_000_000 lines

    dante@dante-pc: time yes | python input.py 1000000
    real    0m3,372s

    dante@dante-pc: time yes | python readline.py 1000000
    real    0m0,130s
    """
    return sys.stdin.readline().strip()

def print(s, end="\n"):
    """
    Faster output in 2 times on 1_000_000 lines
    """
    return sys.stdout.write(str(s) + end)
```
