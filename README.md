
# :bulb: storeless !

> Source code somewhere, static content elsewhere.

---

### :heavy_check_mark: The problem it solves

>Say you have an application hosting provider, offering you a web app or two for free,
but doesn't offer you enough free storage.<br><br>
On the other hand, you have a free service which provides enough storage, but gives little or no features to your app.<br><br>
[storeless](https://github.com/roshnet/storeless) acts as the bridge between both ends of these services. It provides a perfect match by bringing both features of these "free" services at your disposal.


<br>

## storeless Workflow


### In-code use

storeless uses a special configuration file, which needs to be specified when initialising it
in code. Let's suppose you name the file as "storecfg.json", then the actual initialisation will
look like - 
```py
import storeless
...
store = storeless.StoreLess("storecfg.json")
```
It is recommended that the config file not be tracked by a version control system, as it contains
credentials of all associated FTP accounts.
> NOTE: If you do not provide a file name, storeless checks for and uses the filename ".storecfg" by default.

