"""
Fix headers
"""

import sys
import panflute as pf

ignore_elements = []

def stringify(*args):
    for arg in args:
        if isinstance(arg, pf.Space):
            continue
        else:
            yield arg.text

def titlelify(content):
    return "-".join([x.lower() for x in stringify(*content)])

def print(*args):
    for arg in args:
        sys.stderr.write("{}\n".format(str(arg)))
        sys.stderr.flush()

def fix_header_level(elem, doc):
    preblock = []
    if isinstance(elem, pf.Header) and elem.level == 1:
        if doc.is_in_section is True:
            doc.is_in_section = False
            preblock.append(pf.RawBlock("</section>"))
        if 'slide-level' in elem.attributes:
            if doc.is_in_subsection is True:
                doc.is_in_subsection = False
                preblock.append(pf.RawBlock("</section>"))
            if doc.is_first_slide is False:
                preblock.append(pf.RawBlock("""<section id={} class="slide level1">""".format(titlelify(elem.content))))

            doc.is_in_section = True
            doc.is_first_slide = False
            content = elem.content
            elem.content = []
            doc.is_changed = True

            attributes = []
            for k, v in elem.attributes.items():
                attributes.append("data-{}={}".format(k, v))
            s = pf.RawBlock("<section {}>".format(" ".join(attributes)))

            return [
                *preblock,
                s,
                pf.Header(*content, level=2), # TODO: convert to H1?
            ]
        else:
            doc.is_changed = False
            return [
                *preblock,
                elem,
            ]

    if isinstance(elem, pf.Header) and elem.level == 2:
        if doc.is_in_section is True:
            preblock.append(pf.RawBlock("</section>"))
        if doc.is_in_section is True:
            doc.is_in_subsection = True
            attributes = []
            for k, v in elem.attributes.items():
                attributes.append("data-{}={}".format(k, v))
            s = pf.RawBlock("<section {}>".format(" ".join(attributes)))
            return [
                *preblock,
                s,
                elem
            ]

def prepare(doc):
    doc.is_changed = False
    doc.is_in_section = False
    doc.is_in_subsection = False
    doc.is_first_slide = True

def finalize(doc):
    if doc.is_changed is True:
        doc.content.append(pf.RawBlock("</section>"))

def main(doc=None):
    return pf.run_filter(fix_header_level, prepare=prepare, doc=doc, finalize=finalize)


if __name__ == "__main__":
    main()
