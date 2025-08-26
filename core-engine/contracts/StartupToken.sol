// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title StartupToken
 * @dev Token ERC20 pour la tokenisation des startups
 * @notice Permet la création de tokens représentant une participation dans une startup
 */
contract StartupToken is ERC20, Ownable, Pausable, ReentrancyGuard {
    
    // Structure pour stocker les informations de la startup
    struct StartupInfo {
        string name;
        string description;
        uint256 valuation;
        uint256 totalSupply;
        uint256 founderAllocation;
        uint256 teamAllocation;
        uint256 investorAllocation;
        bool isInitialized;
    }
    
    // Informations de la startup
    StartupInfo public startupInfo;
    
    // Mapping des allocations par adresse
    mapping(address => uint256) public allocations;
    
    // Événements
    event StartupInitialized(
        string name,
        uint256 valuation,
        uint256 totalSupply
    );
    
    event TokensAllocated(
        address indexed recipient,
        uint256 amount,
        string allocationType
    );
    
    event ValuationUpdated(uint256 newValuation);
    
    // Modifiers
    modifier onlyWhenInitialized() {
        require(startupInfo.isInitialized, "Startup not initialized");
        _;
    }
    
    modifier onlyFounder() {
        require(allocations[msg.sender] >= startupInfo.founderAllocation, "Not founder");
        _;
    }
    
    /**
     * @dev Constructeur du contrat
     * @param _name Nom de la startup
     * @param _symbol Symbole du token
     */
    constructor(
        string memory _name,
        string memory _symbol
    ) ERC20(_name, _symbol) {
        // Le contrat est créé mais pas encore initialisé
    }
    
    /**
     * @dev Initialise la startup avec les paramètres de base
     * @param _description Description de la startup
     * @param _valuation Valorisation en euros (en centimes)
     * @param _founderAddress Adresse du fondateur
     * @param _teamAddress Adresse de l'équipe
     */
    function initializeStartup(
        string memory _description,
        uint256 _valuation,
        address _founderAddress,
        address _teamAddress
    ) external onlyOwner {
        require(!startupInfo.isInitialized, "Already initialized");
        require(_founderAddress != address(0), "Invalid founder address");
        require(_teamAddress != address(0), "Invalid team address");
        require(_valuation > 0, "Invalid valuation");
        
        startupInfo = StartupInfo({
            name: name(),
            description: _description,
            valuation: _valuation,
            totalSupply: 1_000_000 * 10**decimals(), // 1M tokens avec 18 décimales
            founderAllocation: 200_000 * 10**decimals(), // 20%
            teamAllocation: 100_000 * 10**decimals(),   // 10%
            investorAllocation: 700_000 * 10**decimals(), // 70%
            isInitialized: true
        });
        
        // Allocation des tokens initiaux
        _mint(_founderAddress, startupInfo.founderAllocation);
        _mint(_teamAddress, startupInfo.teamAllocation);
        
        // Enregistrement des allocations
        allocations[_founderAddress] = startupInfo.founderAllocation;
        allocations[_teamAddress] = startupInfo.teamAllocation;
        
        emit StartupInitialized(
            startupInfo.name,
            startupInfo.valuation,
            startupInfo.totalSupply
        );
        
        emit TokensAllocated(_founderAddress, startupInfo.founderAllocation, "Founder");
        emit TokensAllocated(_teamAddress, startupInfo.teamAllocation, "Team");
    }
    
    /**
     * @dev Met à jour la valorisation de la startup
     * @param _newValuation Nouvelle valorisation en euros (en centimes)
     */
    function updateValuation(uint256 _newValuation) external onlyFounder {
        require(_newValuation > 0, "Invalid valuation");
        startupInfo.valuation = _newValuation;
        emit ValuationUpdated(_newValuation);
    }
    
    /**
     * @dev Alloue des tokens à un investisseur
     * @param _investor Adresse de l'investisseur
     * @param _amount Montant de tokens à allouer
     */
    function allocateToInvestor(
        address _investor,
        uint256 _amount
    ) external onlyOwner onlyWhenInitialized nonReentrant {
        require(_investor != address(0), "Invalid investor address");
        require(_amount > 0, "Invalid amount");
        require(
            totalSupply() + _amount <= startupInfo.totalSupply,
            "Exceeds total supply"
        );
        
        _mint(_investor, _amount);
        allocations[_investor] += _amount;
        
        emit TokensAllocated(_investor, _amount, "Investor");
    }
    
    /**
     * @dev Retourne le prix par token en euros
     * @return Prix par token en centimes d'euro
     */
    function getPricePerToken() external view onlyWhenInitialized returns (uint256) {
        return startupInfo.valuation / (startupInfo.totalSupply / 10**decimals());
    }
    
    /**
     * @dev Retourne les informations complètes de la startup
     */
    function getStartupInfo() external view returns (StartupInfo memory) {
        return startupInfo;
    }
    
    /**
     * @dev Retourne l'allocation d'une adresse
     * @param _address Adresse à vérifier
     */
    function getAllocation(address _address) external view returns (uint256) {
        return allocations[_address];
    }
    
    /**
     * @dev Fonction de pause d'urgence (seulement pour le fondateur)
     */
    function pause() external onlyFounder {
        _pause();
    }
    
    /**
     * @dev Fonction de reprise après pause
     */
    function unpause() external onlyFounder {
        _unpause();
    }
    
    /**
     * @dev Override de la fonction transfer pour inclure la pause
     */
    function transfer(
        address to,
        uint256 amount
    ) public virtual override whenNotPaused returns (bool) {
        return super.transfer(to, amount);
    }
    
    /**
     * @dev Override de la fonction transferFrom pour inclure la pause
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public virtual override whenNotPaused returns (bool) {
        return super.transferFrom(from, to, amount);
    }
    
    /**
     * @dev Fonction de récupération d'urgence (seulement pour le fondateur)
     */
    function emergencyWithdraw() external onlyFounder {
        uint256 balance = address(this).balance;
        payable(owner()).transfer(balance);
    }
}