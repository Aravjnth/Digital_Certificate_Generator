from OpenSSL import crypto

def digital_certificate_generator(common_name, country_name, organization_name):
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)
    cert = crypto.X509()
    cert.set_version(2)
    cert.set_serial_number(1)
    cert.set_notBefore(b'20220101000000Z')
    cert.set_notAfter(b'20320101000000Z')
    subject = cert.get_subject()
    subject.C = country_name
    subject.O = organization_name
    subject.CN = common_name
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')
    return cert

cert = digital_certificate_generator("shieldinlix.com", "IN", "shieldinelix Securities Inc.")
print(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode('utf-8'))