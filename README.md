# SolarAssistant Cloud Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

## Install

### Option 1: HACS (Recommended)

1. Go to HACS → Integrations
2. Click "⋮" → Custom repositories
3. Add:
   https://github.com/beerfuzz/solarassistant-cloud
4. Select category: Integration
5. Install

## Setup

After install:

1. Go to Settings → Devices & Services
2. Click "Add Integration"
3. Search for **SolarAssistant Cloud**

## Required Info

- URL: `https://your-instance.us.solar-assistant.io`
- solar_assistant_key: YOUR_KEY
- site_key: YOUR_SITE_KEY

## Notes

- Cookies expire periodically
1. Getting Cookies
	Open SolarAssistant in browser
	Press F12 → Application → Cookies
	Copy:
		_solar_assistant_key
		site_key
- No official API exists
- Uses Grafana backend





