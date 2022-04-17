## NotionCLI

NotionCLI - The CLI tool for Notion.co (https://www.notion.so/ja-jp/product).

## Installation

* To install NotionCLI with pip, run: `pip install notion-cli-py`

## How to use

### Create Integration

To use the notion api, you must create an integration. Please create it [here](https://www.notion.so/my-integrations).

### Setup

After installation, you need to create config file first.
Please run following command.

```
$ notion-cli configure set
```

Then you need to put your integration infomation about the following questions.

```
Are you sure to create config file in /Users/hiratatomonori/.notion_cli? [y/N]: # Type 'y'.
input config label name: # Type your integration name (e.g. "NotionCLI").
input token for NotionCLI: # Type your integration token.
Do you want to set label (LABEL NAME) to current label? [y/N]: # Type 'y' (if this is your first setting).
```

Run following command and check that the configuration is completed properly.

```
### Check if the target page has the integration that set above.
$ notion-cli get pages ${PAGE_ID}
```

If page information can be retrieved the minimum setup is complete.

## Basic Commands

For more detailed information, run `notion-cli <command> - --help` or  `notion-cli <command> <subcommand> - --help`.
### Get (Retrieve) Operations

```
### get pages information
$ notion-cli get pages ${PAGE_IDS}

### get pages properties
$ notion-cli get page_properties ${PAGE_IDS} ${PROPERTY_ID}

### get databases information
$ notion-cli get databases ${DATABASE_IDS}

### get blocks information
$ notion-cli get blocks ${BLOCK_IDS}

### get block children information
$ notion-cli get block_children ${BLOCK_IDS}

### get users information
$ notion-cli get users ${USERS_IDS}

### get all users information
$ notion-cli get all_users
```

### Create Operations

```
### create pages
$ notion-cli create pages ${PALENT_PAGE_IDS} --read-path=${YOUR_FILE_PATH}

### create databases
$ notion-cli create databases ${PALENT_PAGE_IDS} --read-path=${YOUR_FILE_PATH}
```
### Update Operations

```
### update pages
$ notion-cli update pages ${PALENT_PAGE_IDS} --read-path=${YOUR_FILE_PATH}

### update databases
$ notion-cli update databases ${PALENT_PAGE_IDS} --read-path=${YOUR_FILE_PATH}

### update blocks
$ notion-cli update blocks ${PALENT_PAGE_IDS} --read-path=${YOUR_FILE_PATH}
```
### Delete Operations

```
### delete blocks
$ notion-cli delete blocks ${BLOCK_IDS}
```
### Append Operations

```
### append block children
$ notion-cli append block_children ${BLOCK_IDS} --read-path=${YOUR_FILE_PATH}
```

### Configure Operations

```
### set your integration information
$ notion-cli configure set

### show your integration information
$ notion-cli configure show

### switch integration
$ notion-cli configure switch ${LABEL_NAME}
```
### Query Operations

```
### query databases
$ notion-cli query databases ${YOUR_FILE_PATH}
```
### Search Operations

```
### search objects
$ notion-cli search data ${YOUR_FILE_PATH}
```
## License

Licensed under the [MIT](https://github.com/fieldflat/notion-cli-py/blob/main/LISENSE) License.

## Disclaimer

This is **NOT** an official Notion product.
