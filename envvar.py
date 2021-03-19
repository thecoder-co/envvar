def main():
    a = open('/home/idunnuoluwa/.profile', mode='a')
    b = open('/home/idunnuoluwa/.bash_profile', mode='a')
    c = open('/home/idunnuoluwa/.bashrc', mode='a')
    d = open('/etc/profile', mode='a')
    envvar = input('Input the variable in format "VAR_NAME=var":\n')
    a.write('\nexport {}'.format(envvar))
    b.write('\nexport {}'.format(envvar))
    c.write('\nexport {}'.format(envvar))
    d.write('\nexport {}'.format(envvar))

if __name__ == '__main__':
    main()