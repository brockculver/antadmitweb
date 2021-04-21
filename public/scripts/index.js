
const performStudentCreation = document.querySelector("#studentSubmit");

performStudentCreation.addEventListener('click', (e)=>{
  var studentsText=document.getElementById('studentText').value;
  var studentsText=studentsText.split("\n\n\n\n\n\n");
  console.log(studentsText);

  for (var j = 0; j < studentsText.length; j++) {
    console.log(studentsText.length);
      var studentText=studentsText[j].split(",");
      var essay = "";
      for (var i = 14; i < studentText.length; i++) {
        essay=essay+studentText[i];
      }

      console.log(studentText);
      console.log(studentText[0]);
      db.collection("StudentsByBrock").doc(studentText[0]).set({
          name: studentText[0],
          gender: studentText[1],
          sat: studentText[2],
          act: studentText[3],
          GPAunweighted: studentText[4],
          GPAweighted: studentText[5],
          Intendedmajor: studentText[6],
          age: studentText[7],
          race: studentText[8],
          locationCountry: studentText[9],
          locationCity: studentText[10],
          locationState: studentText[11],
          topSport: studentText[12],
          topActivity: studentText[13],
          essay: essay

      }).then(()=>{});
  }
    // document.getElementById('studentText').value="thank you, successfully written";
  })
