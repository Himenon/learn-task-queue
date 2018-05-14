# 検証手順

## 環境

**ホストOS**

macOS High Sierra 10.13.4

**Vagrant**

```
$ vagrant -v
Vagrant 2.0.4
```

**Virtual Box***

5.2.12

**Ansible**

```
$ ansible --version
ansible-playbook 2.4.3.0
```

## 環境構築

コマンドの詳細はMakefileに記載しています。
ここではMakefileの実行コマンドのみ記述します。

### Vagrantを利用する場合

Ansibleを利用して、一発で環境が構築されるようになっています。

```bash
# Vagrantのセットアップ
$ make vm-setup

# ログイン
$ make vm-ssh

# ディレクトリの移動
vagrant$ cd /vagrant
```

VMを破棄する場合(VMからログアウトして下さい)

```bash
$ make vm-clean
```

### macOS上で検証する場合

Docker for Macを立ち上げる。
端末のカレントディレクトリを本ディレクトリにしておく。

## Dockerの操作

```bash
# dockerのセットアップ
$ make docker-setup
```

Redisを起動する場合(Daemonで起動します)

```bash
$ make run-redis
```

ループプロセスを起動する場合(Daemonで起動します)

```bash
$ make run-looper
```

Redisのコンテナに介入する場合

```bash
$ make run-inspector-for-redis
# htop, straceコマンドでプロセスの挙動を確認してみましょう
```

ループプロセスのコンテナに介入する場合

```bash
$ run-inspector-for-looper
# htop, straceコマンドでプロセスの挙動を確認してみましょう
```

コンテナを破棄する場合

```bash
$ make clean
```
