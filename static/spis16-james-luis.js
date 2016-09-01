function get_svg() {
    svg = getProjectSVG(paper);
    $("#content").text(svg);
    document.save_svg_form.submit();
}

function getProjectSVG(paper) {  
     return paper.project.exportSVG({asString:true});
     // or use this if you need it to be "encoded" as "urlsafe"  
     // return encodeURIComponent(paper.project.exportSVG({asString:true}));
  }
