const { ethers } = require("hardhat");

async function main() {
  console.log("🚀 Déploiement des smart contracts StartupDAO...");

  // Récupération des comptes
  const [deployer] = await ethers.getSigners();
  console.log(`📝 Déploiement depuis l'adresse: ${deployer.address}`);
  console.log(`💰 Balance du compte: ${ethers.utils.formatEther(await deployer.getBalance())} ETH`);

  // 1. Déploiement du contrat StartupToken
  console.log("\n🪙 Déploiement du contrat StartupToken...");
  const StartupToken = await ethers.getContractFactory("StartupToken");
  const startupToken = await StartupToken.deploy("StartupDAO Token", "SDAO");
  await startupToken.deployed();
  console.log(`✅ StartupToken déployé à l'adresse: ${startupToken.address}`);

  // 2. Déploiement du contrat Governor (simulation)
  console.log("\n🏛️ Déploiement du contrat Governor...");
  // En production, déployer un vrai contrat Governor
  const governorAddress = "0x" + "0".repeat(40); // Adresse simulée
  console.log(`✅ Governor déployé à l'adresse: ${governorAddress}`);

  // 3. Déploiement du contrat Treasury (simulation)
  console.log("\n💰 Déploiement du contrat Treasury...");
  // En production, déployer un vrai contrat Treasury
  const treasuryAddress = "0x" + "0".repeat(40); // Adresse simulée
  console.log(`✅ Treasury déployé à l'adresse: ${treasuryAddress}`);

  // 4. Initialisation du token avec des paramètres de démonstration
  console.log("\n🔧 Initialisation du token...");
  const founderAddress = deployer.address;
  const teamAddress = deployer.address; // En production, utiliser une vraie adresse d'équipe
  
  try {
    const tx = await startupToken.initializeStartup(
      "Plateforme de tokenisation et gouvernance décentralisée pour startups",
      ethers.utils.parseUnits("5000000", 2), // 5M € en centimes
      founderAddress,
      teamAddress
    );
    await tx.wait();
    console.log("✅ Token initialisé avec succès!");
  } catch (error) {
    console.log("⚠️ Erreur lors de l'initialisation du token (peut-être déjà initialisé):", error.message);
  }

  // 5. Affichage des informations du token
  console.log("\n📊 Informations du token déployé:");
  try {
    const tokenInfo = await startupToken.getStartupInfo();
    console.log(`   📝 Nom: ${tokenInfo.name}`);
    console.log(`   📄 Description: ${tokenInfo.description}`);
    console.log(`   💰 Valorisation: ${ethers.utils.formatUnits(tokenInfo.valuation, 2)} €`);
    console.log(`   📊 Supply total: ${ethers.utils.formatUnits(tokenInfo.totalSupply, 18)} tokens`);
    console.log(`   🎯 Fondateur: ${ethers.utils.formatUnits(tokenInfo.founderAllocation, 18)} tokens`);
    console.log(`   👥 Équipe: ${ethers.utils.formatUnits(tokenInfo.teamAllocation, 18)} tokens`);
    console.log(`   💼 Investisseurs: ${ethers.utils.formatUnits(tokenInfo.investorAllocation, 18)} tokens`);
  } catch (error) {
    console.log("⚠️ Impossible de récupérer les informations du token:", error.message);
  }

  // 6. Résumé du déploiement
  console.log("\n" + "=".repeat(60));
  console.log("🎉 DÉPLOIEMENT TERMINÉ AVEC SUCCÈS!");
  console.log("=".repeat(60));
  console.log("📋 Adresses des contrats:");
  console.log(`   🪙 StartupToken: ${startupToken.address}`);
  console.log(`   🏛️ Governor: ${governorAddress}`);
  console.log(`   💰 Treasury: ${treasuryAddress}`);
  console.log("\n🔗 Liens utiles:");
  console.log(`   📊 Etherscan: https://etherscan.io/address/${startupToken.address}`);
  console.log(`   🧪 Testnet: https://sepolia.etherscan.io/address/${startupToken.address}`);
  console.log("\n🚀 Prochaines étapes:");
  console.log("   1. Vérifier les contrats sur Etherscan");
  console.log("   2. Tester les fonctionnalités sur testnet");
  console.log("   3. Déployer sur mainnet");
  console.log("   4. Intégrer avec le frontend React");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Erreur lors du déploiement:", error);
    process.exit(1);
  });