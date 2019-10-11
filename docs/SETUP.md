## How exactly to use storeless?

Using storeless is easy, but it does require some efforts to create multiple accounts where
data is to be stored. For this example, we'll choose a service which gives a free FTP
account with ~1 GB storage, viz. [000webhost](https://000webhost.com). So, say we have 10 such
accounts, we get 10 GB free storage!

storeless uses a special file called `.storecfg` (you can change it, but you'll also have to reflect the
changes in your code). This file contains the list of all credentials you have for all associated accounts.

A `.storecfg` file looks like -
```json
{
    "files.000webhost.com": {
        "storage-1": "somestringpassword",
        "storage-2": "passwordfortwo"
    },

    "some-other.ftp.host": {
        "account-1": "passwordforacct1",
        "account-2": "passwordforacct2"
    }
}
```

storeless' built-in parser prepares a list of servers from this data, and attempts an upload.

If an upload fails, the next account in the list is tried. This goes on till all the accounts have
been attempted. If you have set the credentials correctly, and haven't exceeded your 1GB storage limit,
then storeless stores data on that account, and returns a URL 
