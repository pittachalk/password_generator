# pwd_generator

This is a simple Python script to generate a random password.

By default, the password follows the style of Apple iCloud Keychain's password generator.
However, this behaviour can be customised as needed.

```
"xxxxxx-xxxxxx-xxxxxx"

where x: random uppercase and lowercase characters or digits
```

To run the script:
```sh
python generate_random_password.py
```

To see additional arguments and options:
```sh
python3 generate_random_password.py -h
```

Requires at least Python 3.6 (needed for `argparse` and `random.choice` functions). 
The script uses entirely built-in modules in Python, so should not require any additional libraries.

You can add this into yout `.zshrc` or `.bash_profile` to create a command line shortcut to use this command.
```sh
# default options
alias generate_random_password="python /path/to/script/generate_random_password.py"

# my preferred settings (for readability)
alias generate_random_password="python /path/to/script/generate_random_password.py --exclude_ambiguous -d 0.15"
```
