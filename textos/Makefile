MEXT = md.txt

# All markdown files in the working directory
SRC = $(wildcard *.$(MEXT))
PDFS= $(addprefix out/, $(SRC:.md.txt=.pdf) )
DOCX= $(addprefix out/, $(SRC:.md.txt=.docx) )

pdf: $(PDFS)
docx: $(DOCX)

all: $(PDFS) out/presentacion_intro.html out/descripcion_cronograma.docx out/descripcion_cronograma.odt

templates/default.revealjs:
		true

out/presentacion_intro.html: presentacion_intro.md.txt templates/default.revealjs
		pandoc --template=templates/default.revealjs  --mathjax -t revealjs presentacion_intro.md.txt -o out/presentacion_intro.html

out/descripcion_cronograma.odt: cronograma_tentativo.md.txt descripcion_proyecto.md.txt  diagrama_general.svg
		pandoc -t odt -o out/descripcion_cronograma.odt descripcion_proyecto.md.txt cronograma_tentativo.md.txt

out/descripcion_cronograma.docx: cronograma_tentativo.md.txt descripcion_proyecto.md.txt  diagrama_general.svg
		pandoc -t docx -o out/descripcion_cronograma.docx descripcion_proyecto.md.txt cronograma_tentativo.md.txt

out/%.pdf: %.md.txt
	pandoc --latex-engine=xelatex --template templates/default.latex --filter pandoc-citeproc --bibliography bib/general.bib -V pagestyle=ath -o $@ $<

out/%.docx: %.md.txt
	pandoc -t docx --filter pandoc-citeproc --bibliography bib/general.bib -o $@ $<
