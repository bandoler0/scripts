O intuito deste programa é criar uma wordlist personalizada para bypassar sistemas de login, intercalando palavras da wordlist com credenciais válidas.
Assim, enquanto realiza-se o brute force, autentica-se periodicamente no sistema, bypassando a proteção de brute-force.

USAR: python3 bypass.py <credencial válida> <posição da credencial> <wordlist>
EXEMPLO: python3 bypass.py password23 2 /usr/share/wordlists/rockyou.txt