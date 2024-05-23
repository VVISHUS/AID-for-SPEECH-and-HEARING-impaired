const asar = require('asar');
const fs = require('fs');
const path = require('path');

const asarFilePath = "C:/Users/asus/AppData/Local/Programs/SiGML-Player/resources/app.asar"
const tempDir =  'C:/Users/asus/AppData/Local/Programs/SiGML-Player/resources/extracted_asar'

asar.extractAll(asarFilePath, tempDir);


// asar.createPackage(tempDir, asarFilePath + '_new')
//   .then(() => {
//     // Replace the original ASAR file with the updated one
//     fs.renameSync(asarFilePath + '_new', asarFilePath);
//     console.log('ASAR file updated successfully.');
//   })
//   .catch((err) => {
//     console.error('Error updating ASAR file:', err);
//   });