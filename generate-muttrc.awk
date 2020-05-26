#!/usr/bin/env -S awk -f

# Invoke like so:
# $ ./generate-muttrc.awk sample.colors template.muttrc > out.muttrc
#
# See https://stackoverflow.com/a/30766470 for more details on how this
# works.

NR==FNR { var2val[$1] = $NF; next }
{
    for (var in var2val) {
        sub("%%"var"%%",var2val[var])
    }
    print
}
