import click
from icmp_sniffer import sniff_icmp

@click.group()
def socket_lab():
    pass

@socket_lab.command()
def cmd1():
    '''Command on socket_lab'''
    click.echo('Placeholder command! Project is still a baby project.')

@socket_lab.command()
def icmp():
    '''Sniff incoming packets for ICMP and displaying type and source IP.'''
    click.echo('Displaying incoming ICMP packets and displaying source IP.')
    click.command(name=sniff_icmp, cls=sniff_icmp)
if __name__ == '__main__':
    socket_lab()
