db.samples.aggregate([
  {
    $match: {
      "diseases": {
        $all: [
          { $elemMatch: { orphanet_id: "ORPHA560" } }, // Sindrome di Marfan
          { $elemMatch: { orphanet_id: "ORPHA363" } }  // Fibrosi Cistica
        ]
      }
    }
  },
  {
    $addFields: {
      collectionYear: { $year: "$collection_date" }
    }
  },
  {
    $group: {
      _id: "$collectionYear",
      sampleCount: { $sum: 1 }
    }
  },
  {
    $group: {
      _id: null,
      totalSamples: { $sum: "$sampleCount" },
      numberOfYears: { $sum: 1 }
    }
  },
  {
    $project: {
      _id: 0,
      averageSamplesPerYear: { $divide: ["$totalSamples", "$numberOfYears"] }
    }
  }
]);