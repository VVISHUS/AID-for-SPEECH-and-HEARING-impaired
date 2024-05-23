asar.createPackage(tempDir, asarFilePath + '_new')
  .then(() => {
    // Replace the original ASAR file with the updated one
    fs.renameSync(asarFilePath + '_new', asarFilePath);
    console.log('ASAR file updated successfully.');
  })
  .catch((err) => {
    console.error('Error updating ASAR file:', err);
  });