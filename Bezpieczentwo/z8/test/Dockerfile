FROM alpine:latest

RUN apk add --no-cache openssh-server

RUN adduser -D testuser && echo "testuser:password123" | chpasswd

RUN ssh-keygen -A

RUN mkdir -p /home/testuser/.ssh && \
    chown -R testuser:testuser /home/testuser/.ssh && \
    chmod 700 /home/testuser/.ssh
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-e", \
     "-o", "PubkeyAuthentication=yes", \
     "-o", "PasswordAuthentication=no", \
     "-o", "KbdInteractiveAuthentication=no", \
     "-o", "PermitEmptyPasswords=no"]