    const exec = require('child_process').exec;
    const lowriter = 'C:/Progra~2/LibreO~1/program/swriter.exe';
    
    const outDir = 'C:/abs_outpath/';
    const srcDir = 'C:/abs_srcpath/';

    let files = ['file1.pdf', 'file2.pdf'];
    files.map(pdffile => {
        let cmd = lowriter + ' --invisible --convert-to docx --outdir "' + outDir + '" "' + srcDir + pdffile '"';
        exec(cmd, function(error, stdout, stderr) {
            // command output is in stdout
        });
    });