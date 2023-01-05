//Bucket Configurations
var bucketName = "fo-softwork-02";
var bucketRegion = "us-east-1";
var IdentityPoolId = 'us-east-1:879f7519-8eee-4923-a1ce-9a34ede8ad79';

// AWS.config.update({
//             region: bucketRegion,
//             credentials: new AWS.CognitoIdentityCredentials({
//                 IdentityPoolId: IdentityPoolId
//         })
//     });

// var s3 = new AWS.S3({
//         apiVersion: '2006-03-01',
//         params: {Bucket: bucketName}
// });

const ID = 'AKIAQV5DXYVEDTUGUPB5';
const SECRET = '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';

const s3 = new AWS.S3({
    accessKeyId: ID,
    secretAccessKey: SECRET
});

const uploadFile = () => {
    // Read content from the file
    const albumName = "dps";
    const username = document.getElementById('username').value;
    const user_id = document.getElementById('user_id').value;
    var files = document.getElementById("fileUpload").files;
    if (!files.length) {
        return alert("Please choose a file to upload first.");
    }
    const file = files[0];
    let size = file.size / 1024 / 1024;
    size = Math.round(size);

    if (size > 1) {
        return alert("picture size should be less than 1mb");
    }
        
    file_types = ["image/png", "image/jpeg", "image/jpg"];

    if (!file_types.includes(file.type))
        return alert("unsupported file type");
    
    var fileName = username + "." + file.name.split(".")[1];

    fetch(
        `http://localhost:5000/api/v1/dp-name/${user_id}/${fileName}`,
        {
            method: 'POST'
        }
    )
    .then((res) => {
        return res.json();
    })
    .then((data) => {
        if (data.success === true) {
            console.log("change effected");
        }
        else if (data.error === true) {
            console.log("an error occured");
        }
        else {
            console.log("change not effected");
        }
    });

    var albumPhotosKey = encodeURIComponent(albumName) + "/";
    var photoKey = albumPhotosKey + fileName;

    // Setting up S3 upload parameters
    const params = {
        Bucket: bucketName,
        Key: photoKey, // File name you want to save as in S3
        Body: file
    };

    // Uploading files to the bucket
    s3.upload(params, function(err, data) {
        if (err) {
            throw err;
        }
        console.log(`File uploaded successfully. ${data.Location}`);
        const url = s3.getSignedUrl('getObject', {
            Bucket: bucketName,
            Key: photoKey,
            Expires: 3600
        });

        document.getElementById("profile_pic").src = url;

        fetch(`http://localhost:5000/api/v1/dp_status/${user_id}`,
            {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ status: true })
            }
        ).then(function (res) {
            return res.json();
        }).then(function (data) {
            if (data.success === true) {
                console.log("user profile picture modified");
            }
            else {
                console.log("user profile picture failed to modify");
            }
        });
        
        console.log(`profile picture updated`);
    });
};


      
