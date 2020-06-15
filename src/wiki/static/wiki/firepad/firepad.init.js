$(document).ready(function () {
  try {
    console.log(editorMetadata);

    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);

    // Get Firebase Database reference.
    var firepadRef = firebase.database().ref().child(editorMetadata.slug);

    // Create CodeMirror (with lineWrapping on).
    var codeMirror = CodeMirror.fromTextArea(document.getElementById("firepad"), {
      mode: "markdown",
      lineWrapping: true,
      lineNumbers: true,
    });

    if (editorMetadata.user === null) {
      editorMetadata.user = "Guest " + Math.floor(Math.random() * 1000);
    } 

    var userId = editorMetadata.user;

    // Create Firepad (with rich text toolbar and shortcuts enabled).
    var firepad = Firepad.fromCodeMirror(firepadRef, codeMirror, {
      defaultText: firepadContent,
      userId: userId,
    });

    var firepadUserList = FirepadUserList.fromDiv(firepadRef.child("users"),
      document.getElementById("userlist"), userId, userId);
  } catch (error) {
    CodeMirror(document.getElementById("firepad"), {
      mode: "markdown",
      lineWrapping: true,
      lineNumbers: true,
    });
  }  
});
