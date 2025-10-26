const appDbName   = process.env.APP_DB_NAME || 'appdb';
const appUser     = process.env.APP_DB_USERNAME || 'app_user';
const appPassword = process.env.APP_DB_PASSWORD || 'app_password';

print(`>> Creating application user '${appUser}' on db '${appDbName}'`);

db = db.getSiblingDB(appDbName);

db.createUser({
  user: appUser,
  pwd: appPassword,
  roles: [{ role: "readWrite", db: appDbName }]
});
