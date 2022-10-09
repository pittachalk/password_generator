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

Requires at least Python 3.5 (needed for `argparse`). 
The script uses entirely built-in modules in Python, so should not require any additional libraries.
