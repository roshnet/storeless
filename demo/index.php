<?php

# Create the directory for first-time use
$UPLOAD_DIR = "uploads/";


if (isset($_FILES)) {
    // var_dump($_FILES);

    if (count($_FILES) == 1) {
        foreach ($_FILES as $name => $props) {
            $outfile = $UPLOAD_DIR.$name;
            if (move_uploaded_file($_FILES[$name]["tmp_name"], $outfile))
                echo "Works!";
            else echo "something went wrong";
        }
    }
    else {
        echo "ERROR: Too many files uploaded at once.";
    }
}
