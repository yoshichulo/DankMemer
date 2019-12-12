# DankMemer

DankMemer is a Python3 Script for downloading memes from the different Reddit subreddits.

## Requirements

You need to install **BeautifulSoup** and **requests** modules.\
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install them.

```bash
pip3 install bs4
pip3 install requests
```

## Usage

```bash
py DankMemer.py -o <output_directory> -s <subreddits>
```

* -o: *(optional)* The folder were the memes will be downloaded (default is *DankMemer*)
* -s: Subreddits you want to download the memes from, separated by a comma.

Example:
```bash
py -o DankMemer.py "MyCuteFolder" -s "memes, dndmemes, dankmemes"
```
Or in case you are a Linux user:
```bash
./DankMemer.py "MyCuteFolder" -s "memes, dndmemes, dankmemes"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
