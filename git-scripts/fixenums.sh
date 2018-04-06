use metadata;
db.device.update({adminState:"locked"},{$set:{adminState:"LOCKED"}},{multi:true} );
db.device.update({adminState:"unlocked"},{$set:{adminState:"UNLOCKED"}},{multi:true} );
db.deviceService.update({adminState:"locked"},{$set:{adminState:"LOCKED"}},{multi:true} );
db.deviceService.update({adminState:"unlocked"},{$set:{adminState:"UNLOCKED"}},{multi:true} );
db.device.update({operatingState:"enabled"},{$set:{operatingState:"ENABLED"}},{multi:true} );
db.device.update({operatingState:"disabled"},{$set:{operatingState:"DISABLED"}},{multi:true} );
db.deviceService.update({operatingState:"enabled"},{$set:{operatingState:"ENABLED"}},{multi:true} );
db.deviceService.update({operatingState:"disabled"},{$set:{operatingState:"DISABLED"}},{multi:true} );