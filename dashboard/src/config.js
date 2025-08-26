// Configuration des URLs de l'API
export const API_CONFIG = {
  // API principale du marketplace
  MARKETPLACE_API: 'http://localhost:5000',
  
  // Endpoints du marketplace
  ENDPOINTS: {
    MARKET: '/market',
    TOKEN_DETAILS: (symbol) => `/market/token/${symbol}`,
    MARKET_STATS: '/market/stats',
    ORDER_BOOK: (symbol) => `/market/orderbook/${symbol}`,
    PRICE_HISTORY: (symbol) => `/market/price-history/${symbol}`,
    HEALTH: '/health'
  },
  
  // API de création de startups (existante)
  STARTUP_API: 'http://localhost:8000',
  STARTUP_ENDPOINTS: {
    CREATE_STARTUP: '/create-startup'
  }
};

// Configuration des graphiques
export const CHART_CONFIG = {
  COLORS: ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884D8'],
  TIME_FRAMES: [7, 30], // jours
  DEFAULT_TIME_FRAME: 7
};

// Configuration du marketplace
export const MARKET_CONFIG = {
  REFRESH_INTERVAL: 30000, // 30 secondes
  MAX_TOKENS_DISPLAY: 50,
  DECIMAL_PLACES: 4
};