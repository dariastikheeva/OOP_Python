class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.info = [self.fio, self.job, self.old, self.salary, self.year_job]

    def __getitem__(self, indx):
        return self.info[indx]
    
    def __setitem__(self, key, value):
        self.info[key] = value
