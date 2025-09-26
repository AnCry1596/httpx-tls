#!/usr/bin/env python3
"""
Example of using httpx-socks with httpx_tls for JA3 modification
"""

import httpx
from httpx_tls.profiles import TLSProfile
from httpx_socks import SyncProxyTransport, AsyncProxyTransport
from python_socks import ProxyType

# Example TLS configuration for JA3 modification
# You can customize this based on your needs
tls_config = TLSProfile(
    # Example configuration - adjust as needed
    ciphers=[
        0x1301,  # TLS_AES_128_GCM_SHA256
        0x1302,  # TLS_AES_256_GCM_SHA384
        0x1303,  # TLS_CHACHA20_POLY1305_SHA256
    ],
    extensions=[
        'server_name',
        'supported_groups',
        'signature_algorithms',
        'application_layer_protocol_negotiation',
    ]
)

def sync_example():
    """Synchronous example with SOCKS proxy and JA3 modification"""

    # Create SOCKS proxy transport with TLS configuration
    transport = SyncProxyTransport(
        proxy_type=ProxyType.SOCKS5,
        proxy_host='127.0.0.1',
        proxy_port=1080,
        tls_config=tls_config  # This enables JA3 modification
    )

    # Use the transport with httpx client
    with httpx.Client(transport=transport) as client:
        response = client.get('https://httpbin.org/get')
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")

async def async_example():
    """Asynchronous example with SOCKS proxy and JA3 modification"""

    # Create async SOCKS proxy transport with TLS configuration
    transport = AsyncProxyTransport(
        proxy_type=ProxyType.SOCKS5,
        proxy_host='127.0.0.1',
        proxy_port=1080,
        tls_config=tls_config  # This enables JA3 modification
    )

    # Use the transport with async httpx client
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.get('https://httpbin.org/get')
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")

def from_url_example():
    """Example using from_url method"""

    # Create transport from URL with TLS config
    transport = SyncProxyTransport.from_url(
        'socks5://127.0.0.1:1080',
        tls_config=tls_config
    )

    with httpx.Client(transport=transport) as client:
        response = client.get('https://httpbin.org/get')
        print(f"Status: {response.status_code}")

if __name__ == "__main__":
    print("Testing SOCKS proxy with JA3 modification...")

    # Run synchronous example
    print("\n=== Sync Example ===")
    try:
        sync_example()
    except Exception as e:
        print(f"Error in sync example: {e}")

    # Run from_url example
    print("\n=== From URL Example ===")
    try:
        from_url_example()
    except Exception as e:
        print(f"Error in from_url example: {e}")

    # For async example, you would need to run:
    # import asyncio
    # asyncio.run(async_example())