// mongo-init/load_biobank_data.js

// Connessione al database
// Quando eseguito tramite Docker con il comando 'mongosh', il contesto 'db' è già disponibile.
const db = db.getSiblingDB('biobankDB'); // Usa il database 'biobankDB'

// Pulisci le collection esistenti (opzionale, utile per re-run dello script)
// Solo se vuoi resettare i dati ogni volta che il container viene ricreato
db.patients.drop();
db.biobanks.drop();
db.sampletypes.drop();
db.diseases.drop();
db.samples.drop();

print("Collection pulite.");

// --- Dati di base per la generazione ---

const patientNames = [
    { first: "Mario", last: "Rossi" }, { first: "Giulia", last: "Verdi" },
    { first: "Luca", last: "Bianchi" }, { first: "Sara", last: "Neri" },
    { first: "Andrea", last: "Gallo" }, { first: "Francesca", last: "Bruno" },
    { first: "Davide", last: "Rizzo" }, { first: "Elena", last: "Ferrari" },
    { first: "Marco", last: "Marini" }, { first: "Laura", last: "Ricci" },
    { first: "Giovanni", last: "Romano" }, { first: "Chiara", last: "Conti" },
    { first: "Simone", last: "Greco" }, { first: "Martina", last: "Esposito" },
    { first: "Federico", last: "Coppola" }, { first: "Anna", last: "Russo" },
    { first: "Paolo", last: "De Luca" }, { first: "Sofia", last: "Costa" },
    { first: "Matteo", last: "Fontana" }, { first: "Aurora", last: "Barbieri" },
    { first: "Leonardo", last: "Moretti" }, { first: "Beatrice", last: "Longhi" },
    { first: "Riccardo", last: "Giordano" }, { first: "Vittoria", last: "Leone" },
    { first: "Francesco", last: "Colombo" }, { first: "Gaia", last: "Caruso" },
    { first: "Edoardo", last: "Mancini" }, { first: "Camilla", last: "Ferri" },
    { first: "Gabriele", last: "Pellegrini" }, { first: "Alice", last: "Bianco" },
    { first: "Lorenzo", last: "Salvi" }, { first: "Viola", last: "Sanna" },
    { first: "Valerio", last: "Amato" }, { first: "Emma", last: "Vitale" },
    { first: "Samuele", last: "Lombardi" }, { first: "Noemi", last: "Mazzanti" },
    { first: "Cristiano", last: "Grassi" }, { first: "Nicole", last: "Silvestri" },
    { first: "Tommaso", last: "Piras" }, { first: "Irene", last: "Serra" },
    { first: "Filippo", last: "Ferraro" }, { first: "Elisa", last: "Cairoli" },
    { first: "Alessio", last: "Santoro" }, { first: "Rebecca", last: "Galli" },
    { first: "Angelo", last: "Orlando" }, { first: "Sofia", last: "Paoletti" },
    { first: "Bruno", last: "D'Angelo" }, { first: "Monica", last: "Donati" },
    { first: "Roberto", last: "Fiore" }, { first: "Daniela", last: "Pietro" }
];

const biobankNames = [
    "Biobanca Universitaria di Milano", "Biobanca Regionale Toscana",
    "Centro Nazionale Biobanche Roma", "Biobanca di Ricerca Napoli",
    "Biobanca Sarda di Precisione"
];

const sampleTypeData = [
    { name: "Whole Blood", description: "Sangue intero con EDTA", loinc_code: "24354-9", loinc_description: "Blood specimen (whole blood)" },
    { name: "Plasma", description: "Plasma ottenuto da centrifugazione", loinc_code: "31208-2", loinc_description: "Plasma specimen" },
    { name: "Serum", description: "Siero ottenuto da coagulazione", loinc_code: "31207-4", loinc_description: "Serum specimen" },
    { name: "DNA", description: "DNA genomico estratto", loinc_code: "2379-3", loinc_description: "DNA" },
    { name: "RNA", description: "RNA totale estratto", loinc_code: "47225-2", loinc_description: "RNA" },
    { name: "Urine", description: "Campione di urina", loinc_code: "3093-0", loinc_description: "Urine specimen" },
    { name: "Tissue Biopsy", description: "Biopsia tissutale", loinc_code: "29267-2", loinc_description: "Tissue specimen" },
    { name: "Saliva", description: "Campione di saliva", loinc_code: "25807-6", loinc_description: "Saliva specimen" },
    { name: "CSF", description: "Liquor cerebrospinale", loinc_code: "24637-7", loinc_description: "Cerebrospinal fluid specimen" },
    { name: "Cell Culture", description: "Cultura cellulare", loinc_code: "11985-6", loinc_description: "Cell culture" }
];

const diseaseData = [
    { name: "Sindrome di Marfan", description: "Disturbo genetico del tessuto connettivo.", orphanet_id: "ORPHA560" },
    { name: "Fibrosi Cistica", description: "Malattia genetica che colpisce le ghiandole esocrine.", orphanet_id: "ORPHA363" },
    { name: "Distrofia Muscolare di Duchenne", description: "Malattia neuromuscolare degenerativa.", orphanet_id: "ORPHA90059" },
    { name: "Corea di Huntington", description: "Malattia neurodegenerativa ereditaria.", orphanet_id: "ORPHA415" },
    { name: "Talassemia Beta", description: "Anemia ereditaria causata da difetti nella produzione di emoglobina beta.", orphanet_id: "ORPHA851" },
    { name: "Neurofibromatosi Tipo 1", description: "Malattia genetica che causa la crescita di tumori lungo i nervi.", orphanet_id: "ORPHA638" },
    { name: "Sindrome di Down", description: "Condizione cromosomica caratterizzata dalla presenza di una copia extra del cromosoma 21.", orphanet_id: "ORPHA264" },
    { name: "Emofilia A", description: "Disturbo emorragico ereditario dovuto alla carenza del fattore VIII di coagulazione.", orphanet_id: "ORPHA309" },
    { name: "Malattia di Gaucher", description: "Malattia da accumulo lisosomiale ereditaria.", orphanet_id: "ORPHA358" },
    { name: "Fenilchetonuria", description: "Disturbo metabolico ereditario che causa l'accumulo di fenilalanina.", orphanet_id: "ORPHA707" }
];

// Funzioni utility per generare dati casuali
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getRandomDate(start, end) {
    const time = new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
    return time;
}

function getRandomVolume() {
    return parseFloat((Math.random() * (10.0 - 0.5) + 0.5).toFixed(2));
}

function getRandomStatus() {
    const statuses = ["Available", "In Use", "Consumed", "Contaminated"];
    return statuses[getRandomInt(0, statuses.length - 1)];
}

const startCollectionDate = new Date();
startCollectionDate.setFullYear(startCollectionDate.getFullYear() - 3); // 3 anni fa
const endCollectionDate = new Date(); // Oggi

// --- Inserimento Dati ---

// 1. Inserimento Biobanche
const biobanks = [];
for (let i = 0; i < 5; i++) {
    const biobank = {
        name: biobankNames[i],
        acronym: biobankNames[i].split(' ').map(n => n[0]).join(''),
        location: `Via Esempio ${i + 1}, Città ${i + 1}`,
        contact_person: `Responsabile ${i + 1}`,
        contact_email: `contact${i}@${biobankNames[i].toLowerCase().replace(/\s/g, '')}.it`,
        phone_number: `+390${getRandomInt(100000000, 999999999)}`,
        establishment_date: getRandomDate(new Date('2000-01-01'), new Date('2020-12-31')),
        certification_status: i % 2 === 0 ? "ISO 20387 Certified" : "Accredited",
        url: `https://www.${biobankNames[i].toLowerCase().replace(/\s/g, '')}.it`,
        notes: `Biobanca di esempio numero ${i + 1}`
    };
    biobanks.push(biobank);
}
db.biobanks.insertMany(biobanks);
print(`Inserite ${biobanks.length} biobanche.`);

const insertedBiobanks = db.biobanks.find().toArray();

// 2. Inserimento Pazienti
const patients = [];
for (let i = 0; i < 50; i++) {
    const patient = {
        first_name: patientNames[i].first,
        last_name: patientNames[i].last,
        date_of_birth: new Date(getRandomInt(1950, 2000), getRandomInt(0, 11), getRandomInt(1, 28)),
        gender: i % 2 === 0 ? "Male" : "Female",
        contact_info: {
            email: `${patientNames[i].first.toLowerCase()}.${patientNames[i].last.toLowerCase()}@example.com`,
            phone: `+393${getRandomInt(10000000, 99999999)}`
        },
        address: {
            street: `Via Fittizia ${i + 1}`,
            city: `Città Fittizia ${i % 10}`,
            zip_code: `001${getRandomInt(10, 99)}`,
            country: "Italy"
        }
    };
    patients.push(patient);
}
db.patients.insertMany(patients);
print(`Inseriti ${patients.length} pazienti.`);

const insertedPatients = db.patients.find().toArray();

// 3. Inserimento Tipi di Campione
const sampleTypes = [];
for (let i = 0; i < sampleTypeData.length; i++) {
    const st = sampleTypeData[i];
    sampleTypes.push(st);
}
db.sampletypes.insertMany(sampleTypes);
print(`Inseriti ${sampleTypes.length} tipi di campione.`);

const insertedSampleTypes = db.sampletypes.find().toArray();

// 4. Inserimento Malattie
const diseases = [];
for (let i = 0; i < diseaseData.length; i++) {
    const d = diseaseData[i];
    diseases.push(d);
}
db.diseases.insertMany(diseases);
print(`Inserite ${diseases.length} malattie.`);

const insertedDiseases = db.diseases.find().toArray();

// 5. Inserimento Campioni
const samples = [];
for (let i = 0; i < 200; i++) {
    const randomPatient = insertedPatients[getRandomInt(0, insertedPatients.length - 1)];
    const randomBiobank = insertedBiobanks[getRandomInt(0, insertedBiobanks.length - 1)];
    const randomSampleType = insertedSampleTypes[getRandomInt(0, insertedSampleTypes.length - 1)];
    const numDiseases = getRandomInt(1, 3); // Ogni campione può avere 1-3 malattie associate
    const sampleDiseases = [];
    const usedDiseaseIndices = new Set();
    while (sampleDiseases.length < numDiseases) {
        const randomIndex = getRandomInt(0, insertedDiseases.length - 1);
        if (!usedDiseaseIndices.has(randomIndex)) {
            const randomDisease = insertedDiseases[randomIndex];
            sampleDiseases.push({
                _id: randomDisease._id,
                name: randomDisease.name,
                orphanet_id: randomDisease.orphanet_id
            });
            usedDiseaseIndices.add(randomIndex);
        }
    }

    const initialVolume = getRandomVolume();
    const currentVolume = parseFloat((initialVolume * (Math.random() * 0.8 + 0.2)).toFixed(2)); // Volume attuale tra 20% e 100% dell'iniziale

    const collectionDate = getRandomDate(startCollectionDate, endCollectionDate);
    const insertionDate = new Date(collectionDate.getTime() + getRandomInt(1, 30) * 24 * 60 * 60 * 1000); // Inserimento 1-30 giorni dopo la raccolta

    const sample = {
        sample_code: `${randomBiobank.acronym}-${(i + 1).toString().padStart(4, '0')}-${randomSampleType.name.substring(0, 3).toUpperCase()}`,
        sample_type: {
            _id: randomSampleType._id,
            name: randomSampleType.name,
            loinc_code: randomSampleType.loinc_code
        },
        diseases: sampleDiseases,
        person_id: randomPatient._id,
        biobank_id: randomBiobank._id,
        collection_date: collectionDate,
        insertion_date_biobank: insertionDate, // Data di inserimento in biobanca
        volume_ml: currentVolume,
        initial_volume_ml: initialVolume,
        storage_location: {
            freezer_id: `FZR-${getRandomInt(1, 5)}`,
            rack_id: `RACK-${String.fromCharCode(65 + getRandomInt(0, 4))}`,
            box_id: `BOX-${getRandomInt(1, 20)}`,
            position_in_box: `${String.fromCharCode(65 + getRandomInt(0, 9))}${getRandomInt(1, 10)}`
        },
        status: getRandomStatus(),
        notes: `Campione generato automaticamente #${i + 1}`,
        aliquots_count: getRandomInt(0, 5),
        last_modified_date: new Date()
    };
    samples.push(sample);
}
db.samples.insertMany(samples);
print(`Inseriti ${samples.length} campioni.`);

print("\n--- Caricamento dati completato! ---");
print("Puoi ora esplorare il database 'biobankDB' con i dati generati.");
print("Esempio: db.patients.find().pretty()");
print("Esempio: db.samples.find().limit(1).pretty()");
print("Esempio: db.samples.countDocuments()");