const appDbName = process.env.APP_DB_NAME || 'appdb';
db = db.getSiblingDB(appDbName);

db.createCollection("users");

db.users.insertMany([
  {
    email: "alice@example.com",
    name: { first: "Alice", last: "Anders" },
    profile: {
      dob: ISODate("1998-03-12T00:00:00Z"),
      phone: "+49 170 1234567",
      address: {
        line1: "Hauptstraße 12",
        city: "Bremen",
        postal_code: "28195",
        country: "DE"
      },
      preferences: {
        newsletter: true,
        languages: ["en", "de"]
      }
    },
    created_at: new Date(),
    updated_at: new Date()
  }
]);

print(">> Sample data seeded.");
