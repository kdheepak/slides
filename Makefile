# add --self-contained for final

revealjs-url := ./reveal.js
slide-theme := white

all: slides

slides:
	pandoc -t revealjs \
	--standalone \
	--template=./static/html/default.revealjs \
	--filter=./scripts/fix-headers.py \
	--no-highlight \
	--slide-level=1 \
	--variable=revealjs-url:$(revealjs-url) \
	--variable=theme:$(slide-theme) \
	--variable=controls:true \
	--variable=controlsTutorial:true \
	--variable=controlsBackArrows:\'faded\' \
	--variable=progress:true \
	--variable=history:false \
	--variable=slideNumber:true \
	--variable=keyboard:true \
	--variable=overview:true \
	--variable=center:true \
	--variable=touch:true \
	--variable=loop:false \
	--variable=shuffle:false \
	--variable=fragments:true \
	--variable=embedded:false \
	--variable=help:true \
	--variable=showNotes:true \
	--variable=autoPlayMedia:false \
	--variable=hideAddressBar:true \
	--variable=viewDistance:4 \
	--variable=width:\"100%\" \
	--variable=height:\"100%\" \
	--variable=margin:0 \
	--variable=minScale:1 \
	--variable=maxScale:1 \
	index.md -o index.html

clean:
	rm index.html

