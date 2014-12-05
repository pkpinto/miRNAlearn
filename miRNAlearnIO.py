# coding: utf-8


def fasta_iter(fastafile):
    """
    Iterator of the records present in a .fasta file. Each record is yielded as
    a tuple containg the title line (without '>') and the sequence itself.
    """
    on_open_record = False
    with open(fastafile, 'r') as fasta:
        for line in fasta:
            line = line.strip()
            if len(line) == 0:
                continue
            elif line[0] == '#':
                continue
            elif line[0] == '>':
                # close old record
                if on_open_record:
                    yield title, sequence.upper()
                # new record
                title = line[1:].rstrip()
                sequence = ''
                on_open_record = True
            else:
                sequence += line.rstrip()
    if on_open_record:
        yield title, sequence.upper()
