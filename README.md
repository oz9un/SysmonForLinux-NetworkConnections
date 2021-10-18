# SysmonForLinux-NetworkConnections
This tool creates a valid SysmonForLinux configuration file according to your banned IP's list.

## Example usage:
Create a configuration file according to your banned IP list:
```bash
python3 main.py all_disabled.xml banneds.txt
```

Run this configuration file with SysmonForLinux:
```bash
sudo sysmon -c final.xml
```
