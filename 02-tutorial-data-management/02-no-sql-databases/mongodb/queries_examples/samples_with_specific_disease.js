db.samples.aggregate([
  {
    $match: {
      diseases: {
        $elemMatch: { orphanet_id: "ORPHA560" }
      }
    }
  },
  {
    $count: "sampleCount"
  }
]);