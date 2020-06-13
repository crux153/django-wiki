$(document).ready(function() {
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  // Get Firebase Database reference.
  var firepadRef = firebase.database().ref();

  // Create CodeMirror (with lineWrapping on).
  var codeMirror = CodeMirror(document.getElementById("firepad"), {
    mode: "markdown",
    lineWrapping: true,
    lineNumbers: true,
  });

  // Create Firepad (with rich text toolbar and shortcuts enabled).
  var firepad = Firepad.fromCodeMirror(firepadRef, codeMirror,
      { defaultText: "Hello, World!" });
});
