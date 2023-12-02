var pdfUrl =  "{{ livre.pdf.url }} ";
    var viewerOptions = {
    conteneur : document.getElementById('pdfViewer'),
  };

    pdfjsLib.getDocument(pdfUrl).promise.then(function(pdfDocument) {
    var pdfViewer = new pdfjsViewer.PDFViewer(viewerOptions) ;
    pdfViewer.setDocument(pdfDocument) ;

    pdfDocument.getPage(1).then(function(page) {
    pdfViewer.scrollPageIntoView({ pageNumber : 1 }) ;
   });
   });

   //alert('zono');
   