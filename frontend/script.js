// Stock Analysis Dashboard JavaScript

class StockAnalysisDashboard {
    constructor() {
        // Use relative URL since frontend is served from the same domain
        this.apiBaseUrl = '';
        this.isAnalyzing = false;
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        const analyzeBtn = document.getElementById('analyzeBtn');
        const companyInput = document.getElementById('companyInput');

        analyzeBtn.addEventListener('click', () => this.startAnalysis());
        companyInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.startAnalysis();
            }
        });
    }

    async startAnalysis() {
        if (this.isAnalyzing) return;

        const companyInput = document.getElementById('companyInput');
        const tickers = companyInput.value.trim();
        
        this.isAnalyzing = true;
        this.showProgress();
        this.hideResults();
        this.hideError();

        try {
            const response = await this.callAnalysisAPI(tickers);
            this.handleAnalysisSuccess(response);
        } catch (error) {
            this.handleAnalysisError(error);
        } finally {
            this.isAnalyzing = false;
        }
    }

    async callAnalysisAPI(tickers) {
        const payload = {
            tickers: tickers ? tickers.split(',').map(t => t.trim().toUpperCase()) : []
        };

        const response = await fetch(`${this.apiBaseUrl}/run-full-analysis/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.detail || `HTTP ${response.status}: ${response.statusText}`);
        }

        return await response.json();
    }

    showProgress() {
        document.getElementById('progressSection').classList.remove('hidden');
        document.getElementById('resultsSection').classList.add('hidden');
        document.getElementById('errorSection').classList.add('hidden');
        
        // Disable the analyze button
        const analyzeBtn = document.getElementById('analyzeBtn');
        analyzeBtn.disabled = true;
        analyzeBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Analyzing...';
        analyzeBtn.classList.add('opacity-50');
    }

    hideProgress() {
        document.getElementById('progressSection').classList.add('hidden');
        
        // Re-enable the analyze button
        const analyzeBtn = document.getElementById('analyzeBtn');
        analyzeBtn.disabled = false;
        analyzeBtn.innerHTML = '<i class="fas fa-play mr-2"></i>Analyze';
        analyzeBtn.classList.remove('opacity-50');
    }

    showResults() {
        document.getElementById('resultsSection').classList.remove('hidden');
        document.getElementById('resultsSection').classList.add('fade-in');
    }

    hideResults() {
        document.getElementById('resultsSection').classList.add('hidden');
        document.getElementById('resultsSection').classList.remove('fade-in');
    }

    showError(message) {
        document.getElementById('errorMessage').textContent = message;
        document.getElementById('errorSection').classList.remove('hidden');
    }

    hideError() {
        document.getElementById('errorSection').classList.add('hidden');
    }

    handleAnalysisSuccess(response) {
        this.hideProgress();
        this.showResults();
        
        // Simulate loading results (in a real implementation, you'd poll for results)
        this.simulateResultsLoading();
        
        console.log('Analysis completed:', response);
    }

    handleAnalysisError(error) {
        this.hideProgress();
        this.showError(error.message);
        console.error('Analysis failed:', error);
    }

    simulateResultsLoading() {
        // In a real implementation, you would poll the backend for actual results
        // For now, we'll simulate the loading and show sample data
        
        const resultCards = [
            'marketResearch', 'financialHealth', 'riskAssessment',
            'investmentAnalysis', 'riskEvaluation',
            'portfolioStrategy', 'investmentRationale', 'finalRecommendation'
        ];

        resultCards.forEach((cardId, index) => {
            setTimeout(() => {
                this.updateResultCard(cardId, this.getSampleData(cardId));
            }, (index + 1) * 1000); // Stagger the loading
        });
    }

    updateResultCard(cardId, data) {
        const contentDiv = document.getElementById(`${cardId}-content`);
        
        contentDiv.innerHTML = `
            <div class="space-y-3">
                ${this.formatResultData(data)}
            </div>
        `;
        
        // Add success animation
        contentDiv.classList.add('fade-in');
    }

    formatResultData(data) {
        if (typeof data === 'string') {
            return `<p class="text-gray-700">${data}</p>`;
        }
        
        if (Array.isArray(data)) {
            // Check if this is a companies array
            if (data.length > 0 && (data[0].company || data[0].company_name)) {
                const companyNames = {
                    'AAPL': 'Apple Inc.',
                    'GOOG': 'Alphabet Inc. (Google)',
                    'ORCL': 'Oracle Corporation',
                    'MSFT': 'Microsoft Corporation',
                    'TSLA': 'Tesla, Inc.',
                    'AMZN': 'Amazon.com, Inc.',
                    'META': 'Meta Platforms, Inc.',
                    'NVDA': 'NVIDIA Corporation'
                };
                
                return data.map(item => {
                    const ticker = item.company || item.company_name;
                    const fullName = companyNames[ticker] || ticker;
                    return this.formatCompanyData(item, fullName);
                }).join('');
            }
            
            return data.map(item => {
                if (typeof item === 'object') {
                    return this.formatObjectData(item);
                }
                return `<p class="text-gray-700">• ${item}</p>`;
            }).join('');
        }
        
        if (typeof data === 'object') {
            return this.formatObjectData(data);
        }
        
        return `<p class="text-gray-700">${data}</p>`;
    }

    formatObjectData(obj) {
        let html = '';
        
        for (const [key, value] of Object.entries(obj)) {
            const formattedKey = key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
            
            if (Array.isArray(value)) {
                html += `
                    <div class="mb-3">
                        <strong class="text-gray-800 text-sm font-semibold">${formattedKey}:</strong>
                        <div class="ml-3 mt-1">
                            ${value.map(item => {
                                if (typeof item === 'object') {
                                    return `<div class="mb-2 p-2 bg-gray-50 rounded">${this.formatObjectData(item)}</div>`;
                                }
                                return `<p class="text-gray-700 text-sm">• ${item}</p>`;
                            }).join('')}
                        </div>
                    </div>
                `;
            } else if (typeof value === 'object' && value !== null) {
                html += `
                    <div class="mb-3">
                        <strong class="text-gray-800 text-sm font-semibold">${formattedKey}:</strong>
                        <div class="ml-3 mt-1 p-2 bg-gray-50 rounded">
                            ${this.formatObjectData(value)}
                        </div>
                    </div>
                `;
            } else {
                html += `
                    <div class="mb-2">
                        <strong class="text-gray-800 text-sm font-semibold">${formattedKey}:</strong>
                        <span class="text-gray-700 text-sm ml-2">${value}</span>
                    </div>
                `;
            }
        }
        
        return html;
    }

    formatCompanyData(company, companyName) {
        let html = '';
        
        // Add company header with prominent styling
        html += `
            <div class="mb-4 p-3 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg border-l-4 border-blue-500">
                <h5 class="text-lg font-bold text-blue-800 mb-2">
                    <i class="fas fa-building mr-2"></i>
                    ${companyName} (${company.company || company.company_name})
                </h5>
            </div>
        `;
        
        // Format company data
        for (const [key, value] of Object.entries(company)) {
            if (key === 'company' || key === 'company_name') continue; // Skip company name as it's already displayed
            
            const formattedKey = key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase());
            
            if (Array.isArray(value)) {
                html += `
                    <div class="mb-3">
                        <strong class="text-gray-800 text-sm font-semibold">${formattedKey}:</strong>
                        <div class="ml-3 mt-1">
                            ${value.map(item => `<p class="text-gray-700 text-sm">• ${item}</p>`).join('')}
                        </div>
                    </div>
                `;
            } else if (typeof value === 'object' && value !== null) {
                html += `
                    <div class="mb-3">
                        <strong class="text-gray-800 text-sm font-semibold">${formattedKey}:</strong>
                        <div class="ml-3 mt-1 p-2 bg-gray-50 rounded">
                            ${this.formatObjectData(value)}
                        </div>
                    </div>
                `;
            } else {
                html += `
                    <div class="mb-2">
                        <strong class="text-gray-800 text-sm font-semibold">${formattedKey}:</strong>
                        <span class="text-gray-700 text-sm ml-2">${value}</span>
                    </div>
                `;
            }
        }
        
        return html;
    }

    getSampleData(cardId) {
        const sampleData = {
            marketResearch: {
                companies: [
                    {
                        company: "AAPL",
                        market_share: "Leading smartphone market with 18.3% global share",
                        competitive_position: "Strong brand loyalty and ecosystem lock-in",
                        key_metrics: [
                            "Revenue growth: 8.1% YoY",
                            "Market cap: $2.8 trillion",
                            "P/E ratio: 28.5",
                            "ROE: 147%",
                            "Operating margin: 30.8%"
                        ],
                        recent_performance: "Strong Q4 earnings beat with iPhone 15 success and services revenue growth of 16.3%"
                    },
                    {
                        company: "GOOG",
                        market_share: "Dominant search market with 91.9% global share",
                        competitive_position: "AI leadership and cloud infrastructure",
                        key_metrics: [
                            "Revenue growth: 12.3% YoY",
                            "Market cap: $1.7 trillion",
                            "P/E ratio: 25.2",
                            "ROE: 23.4%",
                            "Cloud revenue growth: 22.5%"
                        ],
                        recent_performance: "Cloud business growing rapidly with AI integration driving new revenue streams"
                    },
                    {
                        company: "ORCL",
                        market_share: "Leading enterprise software with 31.2% market share",
                        competitive_position: "Database dominance and cloud transformation",
                        key_metrics: [
                            "Revenue growth: 5.2% YoY",
                            "Market cap: $320 billion",
                            "P/E ratio: 31.8",
                            "ROE: 89.2%",
                            "Cloud revenue growth: 45.3%"
                        ],
                        recent_performance: "Strong cloud migration momentum with Cerner acquisition integration"
                    }
                ]
            },
            financialHealth: {
                companies: [
                    {
                        company: "AAPL",
                        financial_ratios: [
                            "ROE: 147.3%",
                            "Debt-to-Equity: 1.5",
                            "Current Ratio: 1.1",
                            "Quick Ratio: 0.9",
                            "Operating Margin: 30.8%"
                        ],
                        analyst_recommendations: [
                            "Buy (15 analysts)",
                            "Strong Buy (8 analysts)",
                            "Hold (3 analysts)",
                            "Average target: $195.50"
                        ],
                        growth_catalysts: [
                            "iPhone 15 Pro success",
                            "Services revenue growth",
                            "AI integration in iOS",
                            "Emerging markets expansion",
                            "Wearables market leadership"
                        ],
                        earnings_summary: "Consistent earnings growth with strong margins, $96.9B in cash reserves, and robust free cash flow generation"
                    },
                    {
                        company: "GOOG",
                        financial_ratios: [
                            "ROE: 23.4%",
                            "Debt-to-Equity: 0.1",
                            "Current Ratio: 2.8",
                            "Quick Ratio: 2.6",
                            "Operating Margin: 25.1%"
                        ],
                        analyst_recommendations: [
                            "Buy (18 analysts)",
                            "Strong Buy (12 analysts)",
                            "Hold (2 analysts)",
                            "Average target: $165.20"
                        ],
                        growth_catalysts: [
                            "AI leadership in search",
                            "Cloud business expansion",
                            "YouTube monetization",
                            "Hardware ecosystem growth",
                            "Enterprise AI solutions"
                        ],
                        earnings_summary: "Strong revenue diversification with cloud and AI driving growth, $119B in cash reserves"
                    },
                    {
                        company: "ORCL",
                        financial_ratios: [
                            "ROE: 89.2%",
                            "Debt-to-Equity: 2.1",
                            "Current Ratio: 0.8",
                            "Quick Ratio: 0.7",
                            "Operating Margin: 41.2%"
                        ],
                        analyst_recommendations: [
                            "Buy (12 analysts)",
                            "Strong Buy (6 analysts)",
                            "Hold (4 analysts)",
                            "Average target: $145.80"
                        ],
                        growth_catalysts: [
                            "Cloud migration acceleration",
                            "Cerner integration benefits",
                            "Database market leadership",
                            "Enterprise AI adoption",
                            "SaaS revenue growth"
                        ],
                        earnings_summary: "Strong cloud transformation with improving margins and recurring revenue growth"
                    }
                ]
            },
            riskAssessment: {
                companies: [
                    {
                        company: "AAPL",
                        market_risks: [
                            "Smartphone market saturation",
                            "Regulatory scrutiny in multiple markets",
                            "Supply chain concentration in China",
                            "Currency fluctuations impact"
                        ],
                        company_specific_risks: [
                            "Supply chain disruptions",
                            "Key person risk (Tim Cook succession)",
                            "Product innovation pressure",
                            "Services antitrust concerns"
                        ],
                        regulatory_risks: [
                            "Antitrust investigations",
                            "Privacy regulations (GDPR, CCPA)",
                            "App Store commission disputes",
                            "Tax avoidance scrutiny"
                        ],
                        current_risks: [
                            "China market exposure (20% of revenue)",
                            "iPhone dependency (52% of revenue)",
                            "Services ecosystem regulation",
                            "Geopolitical tensions"
                        ],
                        overall_risk_level: "Moderate"
                    },
                    {
                        company: "GOOG",
                        market_risks: [
                            "Search market disruption",
                            "AI competition from Microsoft/OpenAI",
                            "Digital advertising slowdown",
                            "Cloud market competition"
                        ],
                        company_specific_risks: [
                            "AI model competition",
                            "YouTube content moderation",
                            "Hardware market challenges",
                            "Talent retention in AI"
                        ],
                        regulatory_risks: [
                            "Antitrust lawsuits",
                            "Privacy regulations",
                            "Content moderation laws",
                            "AI regulation uncertainty"
                        ],
                        current_risks: [
                            "Search advertising decline",
                            "Cloud market share pressure",
                            "AI investment requirements",
                            "Regulatory compliance costs"
                        ],
                        overall_risk_level: "Moderate to High"
                    },
                    {
                        company: "ORCL",
                        market_risks: [
                            "Cloud migration slowdown",
                            "Database market competition",
                            "Enterprise spending cuts",
                            "Technology disruption"
                        ],
                        company_specific_risks: [
                            "Cerner integration challenges",
                            "Legacy system dependencies",
                            "Sales force restructuring",
                            "Product innovation pressure"
                        ],
                        regulatory_risks: [
                            "Healthcare data regulations",
                            "Cloud security requirements",
                            "International data laws",
                            "Antitrust concerns"
                        ],
                        current_risks: [
                            "Cloud transition execution",
                            "Cerner acquisition integration",
                            "Sales cycle lengthening",
                            "Competition from AWS/Azure"
                        ],
                        overall_risk_level: "Moderate"
                    }
                ]
            },
            investmentAnalysis: {
                companies: [
                    {
                        company_name: "AAPL",
                        potential: "High growth potential in services and wearables, with AI integration driving new opportunities",
                        competitive_advantages: "Ecosystem lock-in, brand strength, supply chain efficiency, cash reserves",
                        market_positioning: "Premium segment leader with strong pricing power and customer loyalty"
                    },
                    {
                        company_name: "GOOG",
                        potential: "Strong growth in cloud and AI, with search dominance providing stable cash flow",
                        competitive_advantages: "AI leadership, search monopoly, YouTube dominance, cloud infrastructure",
                        market_positioning: "Technology leader with diversified revenue streams and innovation focus"
                    },
                    {
                        company_name: "ORCL",
                        potential: "Cloud transformation driving growth with enterprise database leadership",
                        competitive_advantages: "Database market dominance, enterprise relationships, cloud infrastructure",
                        market_positioning: "Enterprise software leader transitioning to cloud-first model"
                    }
                ],
                relative_valuations: "AAPL trading at premium to peers (28.5 P/E vs 22.1 average), GOOG at fair value (25.2 P/E), ORCL at slight premium (31.8 P/E) due to cloud growth",
                overall_investment_recommendations: "Strong buy recommendation for AAPL and GOOG, buy for ORCL. Focus on quality companies with strong competitive moats and growth catalysts"
            },
            riskEvaluation: {
                companies: [
                    {
                        company_name: "AAPL",
                        risk_factors: "Moderate regulatory and market risks with manageable company-specific challenges",
                        key_risks: "China exposure, iPhone dependency, regulatory scrutiny, supply chain concentration",
                        impact_on_growth: "Limited impact expected due to strong diversification and cash reserves",
                        management_capability: "Strong management team with proven track record and succession planning",
                        overall_risk_assessment: "Acceptable risk profile with strong mitigation strategies"
                    },
                    {
                        company_name: "GOOG",
                        risk_factors: "Higher regulatory risks balanced by strong competitive position and AI leadership",
                        key_risks: "Antitrust lawsuits, AI competition, search disruption, regulatory compliance",
                        impact_on_growth: "Moderate impact potential but strong innovation pipeline provides offset",
                        management_capability: "Experienced leadership with strong AI and technology expertise",
                        overall_risk_assessment: "Moderate risk with strong competitive advantages"
                    },
                    {
                        company_name: "ORCL",
                        risk_factors: "Moderate execution and integration risks with improving competitive position",
                        key_risks: "Cloud transition execution, Cerner integration, sales cycle, competition",
                        impact_on_growth: "Manageable impact with strong execution track record",
                        management_capability: "Strong leadership with proven cloud transformation experience",
                        overall_risk_assessment: "Moderate risk with improving fundamentals"
                    }
                ],
                overall_risk_assessment: "Portfolio risk is well-managed with diversified exposure across technology sectors and strong company fundamentals"
            },
            portfolioStrategy: {
                companies: [
                    {
                        company_name: "AAPL",
                        percentage_allocation: 35.0,
                        investment_timeframe: "Long-term (5+ years)"
                    },
                    {
                        company_name: "GOOG",
                        percentage_allocation: 30.0,
                        investment_timeframe: "Long-term (5+ years)"
                    },
                    {
                        company_name: "ORCL",
                        percentage_allocation: 20.0,
                        investment_timeframe: "Medium-term (3-5 years)"
                    }
                ]
            },
            investmentRationale: {
                companies: [
                    {
                        company_name: "AAPL",
                        investment_rationale: "Strong ecosystem lock-in, services revenue growth, AI integration potential, and robust cash generation with $96.9B reserves"
                    },
                    {
                        company_name: "GOOG",
                        investment_rationale: "AI leadership position, search dominance providing stable cash flow, cloud growth acceleration, and YouTube monetization potential"
                    },
                    {
                        company_name: "ORCL",
                        investment_rationale: "Cloud transformation momentum, database market leadership, Cerner integration benefits, and enterprise software expertise"
                    }
                ]
            },
            finalRecommendation: {
                portfolio_strategy: {
                    total_allocation: "100%",
                    technology_sector: "85%",
                    cash_reserve: "15%",
                    individual_allocations: [
                        "Apple Inc. (AAPL): 35% - Core holding with strong ecosystem",
                        "Alphabet Inc. (GOOG): 30% - AI leadership and search dominance", 
                        "Oracle Corporation (ORCL): 20% - Cloud transformation play",
                        "Cash Reserve: 15% - For opportunistic purchases and risk management"
                    ],
                    investment_timeframe: "3-5 years",
                    rebalancing_frequency: "Quarterly",
                    risk_profile: "Moderate to Aggressive"
                },
                investment_rationale: "Focus on quality companies with strong competitive moats, proven management teams, and clear growth catalysts in technology sector",
                overall_recommendation: "BUY - Strong long-term growth potential with manageable risks. Recommended investment timeframe: 3-5 years with quarterly rebalancing"
            }
        };

        return sampleData[cardId] || "Analysis completed successfully";
    }
}

// Initialize the dashboard when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new StockAnalysisDashboard();
});

// Add some utility functions for better UX
function showNotification(message, type = 'info') {
    // Create a simple notification system
    const notification = document.createElement('div');
    notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
        type === 'error' ? 'bg-red-500 text-white' : 
        type === 'success' ? 'bg-green-500 text-white' : 
        'bg-blue-500 text-white'
    }`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

// Add keyboard shortcuts
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        document.getElementById('analyzeBtn').click();
    }
});

// Toggle functions for sections and cards
function toggleSection(sectionId) {
    const content = document.getElementById(`${sectionId}-content`);
    const icon = document.getElementById(`${sectionId}-icon`);
    
    if (content.style.display === 'none') {
        content.style.display = 'grid';
        icon.style.transform = 'rotate(0deg)';
    } else {
        content.style.display = 'none';
        icon.style.transform = 'rotate(-90deg)';
    }
}

function toggleCard(cardId) {
    const content = document.getElementById(`${cardId}-content`);
    const icon = document.getElementById(`${cardId}-icon`);
    
    if (content.style.display === 'none') {
        content.style.display = 'block';
        icon.style.transform = 'rotate(0deg)';
    } else {
        content.style.display = 'none';
        icon.style.transform = 'rotate(-90deg)';
    }
}

// Initialize all sections and cards as expanded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize sections
    ['tier1', 'tier2', 'tier3'].forEach(sectionId => {
        const content = document.getElementById(`${sectionId}-content`);
        const icon = document.getElementById(`${sectionId}-icon`);
        if (content && icon) {
            content.style.display = 'grid';
            icon.style.transform = 'rotate(0deg)';
        }
    });
    
    // Initialize cards
    ['marketResearch', 'financialHealth', 'riskAssessment', 
     'investmentAnalysis', 'riskEvaluation', 
     'portfolioStrategy', 'investmentRationale', 'finalRecommendation'].forEach(cardId => {
        const content = document.getElementById(`${cardId}-content`);
        const icon = document.getElementById(`${cardId}-icon`);
        if (content && icon) {
            content.style.display = 'block';
            icon.style.transform = 'rotate(0deg)';
        }
    });
}); 