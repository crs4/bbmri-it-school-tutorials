Extension: SpecimenCustodian
Id: specimen-custodian
Title: "Specimen Custodian"
Description: "An extension to indicate the custodian responsible for the specimen."
* value[x] only Reference(Practitioner or Organization)
* ^context.type = #element
* ^context.expression = "Specimen"

Profile: MySpecimenProfile
Parent: Specimen
Id: my-specimen-profile
Title: "My Custom Specimen Profile"
Description: "A specimen profile extending the base Specimen resource"

* extension contains SpecimenCustodian named custodian 1..1


