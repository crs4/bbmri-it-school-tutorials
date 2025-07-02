db.samples.aggregate([
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
    $sort: { _id: 1 }  // Sort by year ascending
  }
]);