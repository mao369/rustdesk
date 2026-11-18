from pathlib import Path

config = Path("libs/hbb_common/src/config.rs")
source = config.read_text()
original = 'pub const RENDEZVOUS_SERVERS: &[&str] = &["rs-ny.rustdesk.com"];'
replacement = 'pub const RENDEZVOUS_SERVERS: &[&str] = &["127.0.0.1"];'
if source.count(original) != 1:
    raise SystemExit("Unexpected default server configuration; refusing to build")
config.write_text(source.replace(original, replacement))
